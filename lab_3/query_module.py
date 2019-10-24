from db import DB

def print_non():
    for i in range(3):
        print()

def query_compare(oper, container, sourceValue1, sourceValue2):

    set_by_source1 = container.get_edge_set_by_source(sourceValue1.lower().strip())
    set_by_source2 = container.get_edge_set_by_source(sourceValue2.lower().strip())

    source1_props = set()
    for edge in set_by_source1:
        if edge.get_connectionType() == 'has property':
            source1_props.add(edge.get_target().get_value())

    source2_props = set()
    for edge in set_by_source2:
        if edge.get_connectionType() == 'has property':
            source2_props.add(edge.get_target().get_value())

    if oper == 'пересечение':
        print(source1_props & source2_props)
    elif oper == 'xor':
        print(source1_props ^ source2_props)

def query_define_set(container, instance):

    set_by_source = container.get_edge_set_by_source(instance.lower().strip())
    # for edge in set_by_source:
    #     print('value:',edge.get_target().get_value())

    if len(set_by_source) == 0:
        return

    for edge in set_by_source:
        if edge.get_connectionType() == 'ako':
            source = edge.get_target().get_value()
            print(source)
            query_define_set(container, source)

def query_define_instances(container, target):

    set_by_target = container.get_edge_set_by_target(target)

    for edge in set_by_target:
        if edge.get_connectionType() == 'ako':
            if edge.get_source().get_type() == 'set':
                query_define_instances(container, edge.get_source().get_value())
            else:
                print(edge.get_source().get_value())

def query_define_properties(container, camera):

    set_by_source = container.get_edge_set_by_source(camera.lower().strip())

    for edge in set_by_source:
        if edge.get_connectionType() == 'has property':
                print(edge.get_target().get_value())



if __name__ == '__main__':

    fp = 'data_set.json'
    container = DB.get_edgeContainer(fp)
    # query_compare('пересечение', container, 'Nikon Z6', 'Canon EOS 5D Mark IV')
    # query_define_set('Зенит Е')
    # query_define_instances(container, 'Пленочная камера')
    while True:
        print('Выбрать запрос (1-5):')
        print('1. Найти общее или отличие двух камер:')
        print('2. Определить классы к которым относится камера:')
        print('3. Перечислить экземляры, относящиеся к определенному классу: ')
        print('4. Перечислить свойства камеры: ')
        print('5. Завершить программу.')

        choice = input('Поле ввода номера запроса: ')

        if choice == '1':

            print('Необходимо выбрать одну из нижеперечисленных операций:')
            print('1. Общее')
            print('2. Отличие')
            choice = input('Поле ввода номера выбранного типа запроса: ')

            if choice == '1':
                print('Далее необходимо ввести 2 названия камер:')
                camera1 = input('Поле ввода камеры №1: ').lower().strip()
                camera2 = input('Поле ввода камеры №2: ').lower().strip()
                print('Результат: ')
                query_compare(choice, container, camera1, camera2)
                print_non()

            elif choice == '2':
                print('Далее необходимо ввести 2 названия камер:')
                camera1 = input('Поле ввода названия камеры №1: ').lower().strip()
                camera2 = input('Поле ввода названия камеры №2: ').lower().strip()
                print('Результат: ')
                query_compare(choice, container, camera1, camera2)
                print_non()

        elif choice == '2':
            camera = input('Поле ввода названия камеры: ').lower().strip()
            print('Результат: ')
            query_define_set(container, camera)
            print_non()

        elif choice == '3':
            klass = input('Поле ввода названия класса: ').lower().strip()
            print('Результат: ')
            query_define_instances(container, klass)
            print_non()

        elif choice == '4':
            camera = input('Поле ввода названия камеры: ').lower().strip()
            print('Результат: ')
            query_define_properties(container, camera)
            print_non()

        elif choice == '5':
            break