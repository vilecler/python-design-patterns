from factories import loader

if __name__ == '__main__':
    for factory_name in ['developer_factory', 'cooker_factory', 'butcher_factory']:
        factory = loader.load_factory(factory_name)
        human = factory.create_human()

        print(f"Human name is {human.name!r}")

        human.present()
        human.drink()
        human.eat()
        human.work()
        human.sleep()

        print()
