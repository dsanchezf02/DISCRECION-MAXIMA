from diffusers import DDIMPipeline, DDIMScheduler
import datetime

device = "cuda"

# Introduir ruta del model de generació
pipeline = DDIMPipeline.from_pretrained(f"/Users/diegosanchezfreire/Desktop/DISCRECIÓN MÁXIMA/ENTREGA TFG/Prototip/1. Generació d'imatges/MODEL", local_files_only=True)
pipeline.scheduler = DDIMScheduler.from_config(pipeline.scheduler.config)
pipeline.to(device)

# Generació d'imatges
image = pipeline(num_inference_steps=100).images[0]

current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M")

# Directori on es guardaran les imatges
filename = f"/Users/diegosanchezfreire/Desktop/DISCRECIÓN MÁXIMA/ENTREGA TFG/Prototip/1. Generació d'imatges/RESULTATS"
image.save(filename)