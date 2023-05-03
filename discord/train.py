import subprocess
import os

print(os.getcwd())
print(os.path.exists('../train.py'))
print(os.path.exists('config.py'))

subprocess.run(['python ../train.py config.py --device=cpu --compile=False --eval_iters=20\
 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000\
  --lr_decay_iters=2000 --dropout=0.0'], cwd=os.getcwd())


#python train.py discord/config.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0