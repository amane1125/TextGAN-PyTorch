from __future__ import print_function
import argparse
import config as cfg
from instructor.leakgan_instructor import LeakGANInstructor
from instructor.seqgan_instructor import SeqGANInstructor
from instructor.relgan_instructor import RelGANInstructor


def program_config(parser):
    parser.add_argument('--run_model', default=cfg.run_model, type=str)
    parser.add_argument('--mle_epoch', default=cfg.MLE_train_epoch, type=int)
    parser.add_argument('--adv_epoch', default=cfg.ADV_train_epoch, type=int)
    parser.add_argument('--inter_epoch', default=cfg.inter_epoch, type=int)
    parser.add_argument('--batch_size', default=cfg.batch_size, type=int)
    parser.add_argument('--adv_g_step', default=cfg.ADV_g_step, type=int)
    parser.add_argument('--rollout_num', default=cfg.rollout_num, type=int)
    parser.add_argument('--d_step', default=cfg.d_step, type=int)
    parser.add_argument('--d_epoch', default=cfg.d_epoch, type=int)
    parser.add_argument('--adv_d_step', default=cfg.ADV_d_step, type=int)
    parser.add_argument('--adv_d_epoch', default=cfg.ADV_d_epoch, type=int)
    parser.add_argument('--gen_lr', default=cfg.gen_lr, type=float)
    parser.add_argument('--dis_lr', default=cfg.dis_lr, type=float)

    parser.add_argument('--cuda', default=cfg.CUDA, type=int)
    parser.add_argument('--device', default=cfg.device, type=int)
    parser.add_argument('--ora_pretrain', default=cfg.oracle_pretrain, type=int)
    parser.add_argument('--gen_pretrain', default=cfg.gen_pretrain, type=int)
    parser.add_argument('--dis_pretrain', default=cfg.dis_pretrain, type=int)
    parser.add_argument('--log_file', default=cfg.log_filename, type=str)
    parser.add_argument('--tips', default=cfg.tips, type=str)

    return parser


# MAIN
if __name__ == '__main__':
    # Hyper Parameters
    parser = argparse.ArgumentParser()
    parser = program_config(parser)
    opt = parser.parse_args()
    cfg.init_param(opt)

    # ==========Dict==========
    instruction_dict = {
        'leakgan': LeakGANInstructor,
        'seqgan': SeqGANInstructor,
        'relgan': RelGANInstructor,
    }

    inst = instruction_dict[cfg.run_model](opt)
    inst._run()

    try:
        inst.log.close()
    except:
        pass