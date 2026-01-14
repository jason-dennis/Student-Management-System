class Sorter:
    def insertion_sort(lista, key=lambda x: x, reverse=False):
        """
        Sorts a list using insertion sort.
        :param key:
        :param reverse:
        :return:
        """
        for i in range(1, len(lista)):
            current = lista[i]
            j = i - 1

            while j >= 0:
                if reverse:
                    condition = key(lista[j]) < key(current)
                else:
                    condition = key(lista[j]) > key(current)

                if not condition:
                    break

                lista[j + 1] = lista[j]
                j -= 1

            lista[j + 1] = current

        return lista

    def comb_sort(lista, key=lambda x: x, reverse=False):
        """
        Sorts a list using comb sort.
        """
        gap = len(lista)
        shrink = 1.3
        sorted_flag = False

        while not sorted_flag:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted_flag = True

            i = 0
            while i + gap < len(lista):
                if reverse:
                    condition = key(lista[i]) < key(lista[i + gap])
                else:
                    condition = key(lista[i]) > key(lista[i + gap])

                if condition:
                    lista[i], lista[i + gap] = lista[i + gap], lista[i]
                    sorted_flag = False

                i += 1

        return lista
