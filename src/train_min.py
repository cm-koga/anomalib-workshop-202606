from anomalib.engine import Engine
from anomalib.data import get_datamodule
from anomalib.models import get_model

from omegaconf import OmegaConf
from pathlib import Path

model_cfg_path = "config/patchcore.yaml"
data_cfg_path = "config/wood_min.yaml"
output_dir = "outputs"

model_cfg = OmegaConf.load(model_cfg_path)
data_cfg = OmegaConf.load(data_cfg_path)

data= get_datamodule(data_cfg.data)
model = get_model(model_cfg.model) 

engine = Engine(
    default_root_dir=output_dir,
)

engine.train(model=model, datamodule=data)

print("Train finished.")
