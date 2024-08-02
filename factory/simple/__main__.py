from human_factory import HumanFactory

if __name__ == '__main__':
    factory = HumanFactory()

    for human_name in ['Painter', 'Cooker', 'Developer', 'Painter', 'Butcher']:
        human = factory.create_instance(human_name)
        human.present()
        human.drink()
        human.eat()
        human.work()
        human.sleep()
        print()
