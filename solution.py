#!/usr/bin/python
import sys
import numpy as np

def main():
    input_dir, output_dir = sys.argv[1:]
    
    # how to load data
    data_val = np.load(input_dir + '/data_val.npz', allow_pickle=True)
    N_val = len(data_val['EnergyDeposit'])

    data_test = np.load(input_dir + '/data_test.npz', allow_pickle=True)
    N_test = len(data_test['EnergyDeposit'])

    # just some random predictions, still valid
    np.savez_compressed(output_dir + '/data_val_prediction.npz', 
                        ParticlePoint=np.random.randn(N_val, 2), 
                        ParticleMomentum=np.random.randn(N_val, 2))

    np.savez_compressed(output_dir + '/data_test_prediction.npz', 
                        ParticlePoint=np.random.randn(N_test, 2),
                        ParticleMomentum=np.random.randn(N_test, 2))
    return 0

if __name__ == "__main__":
    main()
