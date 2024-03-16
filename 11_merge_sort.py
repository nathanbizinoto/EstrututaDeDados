if len(lista) >1:
    meio = len(lista) // 2
    sublista_esq = lista[:meio]
    sublista_dir = lista[:meio]

    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    pos_esq = post_dir = 0
    ordenada = []

    while pos_esq < len(sublista_esq) and post_dir < len(sublista_dir):
            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
                ordenada.append(sublista_esq[pos_esq])
                pos_esq += 1

            else:
                ordenada.append(sublista_dir[pos_dir])
                pos_dir += 1

                sobra = []

                if pos_esq < pos_dir: sobra = sublista_esq[pos_dir:]

        return ordenada + sobra
