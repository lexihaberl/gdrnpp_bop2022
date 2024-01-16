# encoding: utf-8
"""This file includes necessary params, info."""
import os
import mmcv
import os.path as osp

import numpy as np

# ---------------------------------------------------------------- #
# ROOT PATH INFO
# ---------------------------------------------------------------- #
cur_dir = osp.abspath(osp.dirname(__file__))
root_dir = osp.normpath(osp.join(cur_dir, ".."))
# directory storing experiment data (result, model checkpoints, etc).
output_dir = osp.join(root_dir, "output")

data_root = osp.join(root_dir, "datasets")
bop_root = osp.join(data_root, "BOP_DATASETS/")

dataset_root = osp.join(bop_root, "ycb_ichores")

train_pbr_dir = osp.join(dataset_root, "train_pbr")

test_dir = osp.join(dataset_root, "test")

test_scenes = [i for i in range(0, 3)]
train_pbr_scenes = [i for i in range(0, 49 + 1)]

model_dir = osp.join(dataset_root, "models")

vertex_scale = 0.001

# object info
id2obj = {
    1: "001_chips_can",  # Add your coordinates here
    2: "002_master_chef_can",  # Add your coordinates here
    3: "003_cracker_box",  # Add your coordinates here
    4: "004_sugar_box",  # Add your coordinates here
    5: "005_tomato_soup_can",  # Add your coordinates here
    6: "006_mustard_bottle",  # Add your coordinates here
    7: "008_pudding_box",  # Add your coordinates here
    8: "009_gelatin_box",  # Add your coordinates here
    9: "010_potted_meat_can",  # Add your coordinates here
    10: "011_banana",  # Add your coordinates here
    11: "013_apple",  # Add your coordinates here
    12: "014_lemon",  # Add your coordinates here
    13: "015_peach",  # Add your coordinates here
    14: "016_pear",  # Add your coordinates here
    15: "017_orange",  # Add your coordinates here
    16: "018_plum",  # Add your coordinates here
    17: "021_bleach_cleanser",  # Add your coordinates here
    18: "024_bowl",  # Add your coordinates here
    19: "025_mug",  # Add your coordinates here
    20: "029_plate"  # Add your coordinates here
}
objects = list(id2obj.values())

obj_num = len(id2obj)
obj2id = {_name: _id for _id, _name in id2obj.items()}

model_paths = [osp.join(model_dir, "obj_{:06d}.ply").format(_id) for _id in id2obj]  # TODO: check this
texture_paths = [osp.join(model_dir, "obj_{:06d}.png".format(_id)) for _id in id2obj]
model_colors = [((i + 1) * 10, (i + 1) * 10, (i + 1) * 10) for i in range(obj_num)]  # for renderer

# yapf: disable
diameters = np.array([252.80359594, 171.97243923, 269.5049832, 198.54678365,
                    120.54337759, 196.52766223, 142.60827776, 113.99714114,
                    129.48072679, 197.83544437, 84.23703614, 68.93023656,
                    63.86475039, 104.12554293, 74.55294161, 57.48756382,
                    259.43381601, 161.95294488, 125.0486685, 261.46419972]) / 1000.0
# yapf: enable
# Camera info
width = 640
height = 480
zNear = 0.25
zFar = 6.0
center = (height / 2, width / 2)

camera_matrix = uw_camera_matrix = np.array([[572.411363389757, 0.0, 325.2611083984375], [0.0, 573.5704328585578, 242.04899588216654], [0.0, 0.0, 1.0]])

depth_factor = 10000.0


def get_models_info():
    """key is str(obj_id)"""
    models_info_path = osp.join(model_dir, "models_info.json")
    assert osp.exists(models_info_path), models_info_path
    models_info = mmcv.load(models_info_path)  # key is str(obj_id)
    return models_info


def get_fps_points():
    """key is str(obj_id) generated by
    core/gdrn_modeling/tools/ycbv/ycbv_1_compute_fps.py."""
    fps_points_path = osp.join(model_dir, "fps_points.pkl")
    assert osp.exists(fps_points_path), fps_points_path
    fps_dict = mmcv.load(fps_points_path)
    return fps_dict


def get_keypoints_3d():
    """key is str(obj_id) generated by
    core/roi_pvnet/tools/ycbv/ycbv_1_compute_keypoints_3d.py."""
    keypoints_3d_path = osp.join(model_dir, "keypoints_3d.pkl")
    assert osp.exists(keypoints_3d_path), keypoints_3d_path
    kpts_dict = mmcv.load(keypoints_3d_path)
    return kpts_dict
