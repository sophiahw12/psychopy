from view import View
from model import Model
from controller import Controller

def main():
    model = Model()
    view = View(model)
    controller = Controller(model=model, dir='img_folder', time=2, num=30)
    controller.start()

if __name__ == "__main__":
    main()
