from mmcv import Config
import os.path as osp
import os
from tqdm import tqdm
import sys
import yaml

cur_dir = osp.normpath(osp.dirname(osp.abspath(__file__)))
PROJ_ROOT = osp.normpath(osp.join(cur_dir, "../../../.."))
sys.path.insert(0, PROJ_ROOT)

base_cfg_name = "002_master_chef_can.py"
base_obj_name = "002_master_chef_can"

# -----------------------------------------------------------------
object_id_file = osp.join(PROJ_ROOT, 'configs/gdrn/ycbv/ycbv.yaml')
with open(object_id_file, 'r') as stream:
    data_loaded = yaml.safe_load(stream)
id2obj = data_loaded["names"]
obj2id = {_name: _id for _id, _name in id2obj.items()}


def main():
    base_cfg_path = osp.join(cur_dir, base_cfg_name)
    assert osp.exists(base_cfg_path), base_cfg_path  # make sure base cfg is in this dir
    cfg = Config.fromfile(base_cfg_path)

    for obj_id, obj_name in tqdm(id2obj.items()):
        print(obj_name)
        if obj_name == base_obj_name:
            continue
        # NOTE: what fields should be updated ---------------------------
        new_cfg_dict = dict(
            _base_="./{}".format(base_cfg_name),
            OUTPUT_DIR=cfg.OUTPUT_DIR.replace(base_obj_name, obj_name),
            DATASETS=dict(
                TRAIN=("ycbv_{}_train_pbr".format(obj_name),),
            ),
        )
        # ----------------------------------------------------------------------
        new_cfg_path = osp.join(cur_dir, base_cfg_name.replace(base_obj_name, obj_name))
        if osp.exists(new_cfg_path):
            raise RuntimeError("new cfg exists!")
        new_cfg = Config(new_cfg_dict)
        with open(new_cfg_path, "w") as f:
            f.write(new_cfg.pretty_text)

    # re-format
    os.system("black -l 120 {}".format(cur_dir))


if __name__ == "__main__":
    main()
