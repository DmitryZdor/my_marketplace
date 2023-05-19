def client_message(object):
    res = (f'Добрый день, {object.first_name} {object.last_name} спасибо что обратились к нам.\n'
            f'В ближайшее время с Вами свяжется наш менеджер, пока проверьте введенные Вами данные:\n'
            f'Адрес {object.address} и телефон {object.phone}\n '
            f'Сумма заказа {object.shopping_cart_history["total_sum"]}\n{"-"*100}\n')
    for el in object.shopping_cart_history['purchased_items']:
        res += ('Наименование: {}  | количество - {} шт.  |   цена-{} руб. | сумма {} руб. |\n').format(
                                                        *[a for a in el.values()]) + f'{"-"*100}\n '

    return res


