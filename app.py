import multiprocessing
import onnxruntime
from torchvision import transforms
import torch
import torch.nn.functional as F
import gradio as gr

sess_options = onnxruntime.SessionOptions()
ort_sess = onnxruntime.InferenceSession("RFNet.onnx", providers=["CPUExecutionProvider"])


preprocess_img = transforms.Compose([
        transforms.Resize((352,352)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])

preprocess_depth = transforms.Compose([
        transforms.Resize((352,352)),
        transforms.ToTensor()])
def inference(img,depth,GT):
    h,w = img.size
    img = preprocess_img(img).unsqueeze(0)
    depth = preprocess_depth(depth.convert('L')).unsqueeze(0)
    ort_inputs = {ort_sess.get_inputs()[0].name: img.numpy(), ort_sess.get_inputs()[1].name: depth.numpy()}
    ort_outs = ort_sess.run(None, ort_inputs)
    output_image   = torch.tensor(ort_outs[0])
    res     = F.interpolate(output_image, size=(w,h), mode='bilinear', align_corners=False)
    res     = torch.sigmoid(res)
    res     = res.data.cpu().numpy().squeeze()
    res     = (res - res.min()) / (res.max() - res.min() + 1e-8)
    return res






title = "Robust RGB-D Fusion for Saliency Detection"
description = """ Deployment of the paper: 
[Robust RGB-D Fusion for Saliency Detection](https://arxiv.org/pdf/2208.01762.pdf) 
published at the International Conference on 3D Vision 2022 (3DV 2022). 
Paper Code can be found at [Zongwei97/RFNet](https://github.com/Zongwei97/RFnet).
Deployed Code can be found at [shriarul5273/Robust_RGB-D_Saliency_Detection](https://github.com/shriarul5273/Robust_RGB-D_Saliency_Detection).
Use example Image and corresponding Depth Map (from NJU2K dataset) or upload your own Image and Depth Map.
"""
article = """ # Citation 
If you find this repo useful, please consider citing:
```
@article{wu2022robust,
  title={Robust RGB-D Fusion for Saliency Detection},
  author={Wu, Zongwei and Gobichettipalayam, Shriarulmozhivarman and Tamadazte, Brahim and Allibert, Guillaume and Paudel, Danda Pani and Demonceaux, Cedric},
  journal={3DV},
  year={2022}
}
```
"""
examples = [['images/image_1.jpg','images/depth_1.png','images/gt_1.png'],
            ['images/image_2.jpg','images/depth_2.png','images/gt_2.png'],
            ['images/image_3.jpg','images/depth_3.png','images/gt_3.png'],
            ['images/image_4.jpg','images/depth_4.png','images/gt_4.png'],
            ['images/image_5.jpg','images/depth_5.png','images/gt_5.png']]

input_1 = gr.Image(type='pil', label="RGB Image", source="upload")
input_2 = gr.Image(type='pil', label="Depth Image", source="upload")
input_3 = gr.Image(type='pil', label="Ground Truth", source="upload")
outputs = gr.Image(type="pil", label="Saliency Map")


gr.Interface(inference, inputs=[input_1,input_2,input_3], outputs=outputs,
                title=title,examples=examples,
                description=description,
                article=article,cache_examples=False).launch(server_name="0.0.0.0", server_port=7000)