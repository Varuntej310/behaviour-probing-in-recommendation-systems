# shuffle_seqs.py
import argparse
import numpy as np
from collections import defaultdict

def shuffle_dataset(input_path, output_path):
    user_seqs = defaultdict(list)
    
    with open(input_path, 'r') as f:
        for line in f:
            u, i = line.strip().split()
            user_seqs[int(u)].append(int(i))
    
    with open(output_path, 'w') as f:
        for u, seq in user_seqs.items():
            np.random.shuffle(seq)  
            for i in seq:
                f.write(f"{u} {i}\n")
    
    print(f"Created {output_path} successfully.")



    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Shuffle user interaction sequences")
    parser.add_argument('--dataset', required=True, 
                       help='Dataset name (e.g., ml-1m, Beauty, Steam, wikipedia)')
    parser.add_argument('--input_dir', default='data', help='Input directory')
    parser.add_argument('--output_dir', default='data', help='Output directory')
    
    args = parser.parse_args()
    
    input_path = f'{args.input_dir}/{args.dataset}.txt'
    output_path = f'{args.output_dir}/{args.dataset}_shuffled.txt'
    
    shuffle_dataset(input_path, output_path)