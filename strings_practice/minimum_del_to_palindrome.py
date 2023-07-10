#import MiniDeletions

#import trash.MiniDeletions

from trash import MiniDeletions

if __name__ == "__main__":
    print("__name__,", __name__)

    text = input()
    minidel = MiniDeletions()

    print("minimum deletions ",minidel.mini_deletions(text))
    





