import argparse
import torchvision.datasets as dsets

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="mnist")
    args = parser.parse_args()

    dataset = args.dataset.lower()

    if dataset == "mnist":
        dsets.MNIST(root="./data", train=True, download=True)
        dsets.MNIST(root="./data", train=False, download=True)

    elif dataset == "kmnist":
        dsets.KMNIST(root="./data", train=True, download=False)
        dsets.KMNIST(root="./data", train=False, download=False)