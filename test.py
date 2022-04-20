import requests
r = requests.post('http:localhost:8000/denseCaptionCreate/', json={
  "opt": {
    "output_dir": "string",
    "num_to_draw": 0,
    "final_nms_thresh": 0,
    "use_cudnn": 0,
    "text_size": 0,
    "max_images": 0,
    "gpu": 0,
    "splits_json": "string",
    "vg_img_root_dir": "string",
    "checkpoint": "string",
    "num_proposals": 0,
    "rpn_nms_thresh": 0,
    "image_size": 0,
    "input_image": "string",
    "input_split": "string",
    "box_width": 0,
    "input_dir": "string",
    "output_vis_dir": "string",
    "output_vis": 0
  },
  "results": [
    {
      "img_name": "test6",
      "scores": [
        0
      ],
      "captions": [
        "string"
      ],
      "boxes": [
        [
          0
        ]
      ]
    }
  ]
})
print(f"Status Code: {r.status_code}, Response: {r.json()}")