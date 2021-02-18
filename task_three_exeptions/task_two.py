
def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except ValueError as e:
        return f'Incorrect data: {e}'
    except TypeError as e:
        return f'Incorrect type: {e}'

    if max_discount > 99:
        raise ValueError('discount')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount /100)


if __name__ == '__main__':
    assert 900.0 == discounted(1000, 10)
    assert "Incorrect type: float() argument must be a string " \
           "or a number, not 'list'" == discounted([5], 10)
    assert "Incorrect data: could not convert string " \
           "to float: '100s'" == discounted('100s', 10)
