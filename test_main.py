from torch.utils.data import DataLoader
import torch.optim as optim
import torch
from utils import save_best_record
from model import Model
from dataset import Dataset

from train import train
from test_10crop import test
import option
from tqdm import tqdm
from utils import Visualizer
from config import *
import torchvision.transforms as transforms



# viz = Visualizer(env='smart survillance', use_incoming_socket=False)

if __name__ == '__main__':
    args = option.parser.parse_args()
    config = Config(args)
    


    test_loader = DataLoader(Dataset(args, test_mode=True),
                              batch_size=1, shuffle=False,
                              num_workers=0, pin_memory=False)


    # print(len(test_loader))

    print('loading model')
    # model = Model(args.feature_size, args.batch_size)
    state_dict = torch.load(args.test_model_path)
    # model_params = state_dict['rtfm295_i3d.pkl'] # replace 'model' with the actual key name that maps to the model's parameters in the saved state dict
    model = Model(args.feature_size, args.batch_size)
    model.load_state_dict(state_dict)




    # for name, value in model.named_parameters():
    #     print(name)


    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

    # if not os.path.exists('./ckpt'):
    #     os.makedirs('./ckpt')

    optimizer = optim.Adam(model.parameters(),
                            lr=config.lr[0], weight_decay=0.005)

    test_info = {"epoch": [], "test_AUC": []}
    best_AUC = -1
    output_path = '/home/aishaeld/scratch/RTFM/output' 
    auc = test(test_loader, model, args, device)

    # auc = test(test_loader, model, args, viz, device)

    # print(f'max epoch is {args.max_epoch}')
    for step in tqdm(
            range(1, args.max_epoch + 1),
            total=args.max_epoch,
            dynamic_ncols=True
    ):
        print(step)
        # if step > 1 and config.lr[step - 1] != config.lr[step - 2]:
        #     for param_group in optimizer.param_groups:
        #         param_group["lr"] = config.lr[step - 1]


        # if (step - 1) % len(train_nloader) == 0:
        #     loadern_iter = iter(train_nloader)

        # if (step - 1) % len(train_aloader) == 0:
        #     loadera_iter = iter(train_aloader)

       

        # # train(loadern_iter, loadera_iter, model, args.batch_size, optimizer, viz, device)
        # train(loadern_iter, loadera_iter, model, args.batch_size, optimizer, device)
        # # train(video_cropsn_n, video_cropsn_a, model, args.batch_size, optimizer, device)

        # if step % 5 == 0 and step > 200:

        # auc = test(test_loader, model, args, viz, device)
        auc = test(test_loader, model, args, device)

        test_info["epoch"].append(step)
        test_info["test_AUC"].append(auc)

        if test_info["test_AUC"][-1] > best_AUC:
            best_AUC = test_info["test_AUC"][-1]
            torch.save(model.state_dict(), './ckpt/' + args.model_name + '{}-i3d.pkl'.format(step))
            save_best_record(test_info, os.path.join(output_path, '{}-step-AUC.txt'.format(step)))

    # torch.save(model.state_dict(), './ckpt/' + args.model_name + 'final.pkl')

