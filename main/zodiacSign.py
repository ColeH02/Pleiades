def zodiac_sign(month, day):

    if month == 12:
        if day < 21:
            sign = 'Sagittarius'
        else:
            sign = 'Capricorn'

    elif month == 1:
        if day < 20:
            sign = 'Capricorn'
        else:
            sign = 'Aquarius'

    elif month == 2:
        if day < 18:
            sign = 'Aquarius'
        else:
            sign = 'Pisces'

    elif month == 3:
        if day < 20:
            sign = 'Pisces'
        else:
            sign = 'Aries'

    elif month == 4:
        if day < 19:
            sign = 'Aries'
        else:
            sign = 'Taurus'

    elif month == 5:
        if day < 20:
            sign = 'Taurus'
        else:
            sign = 'Gemini'

    elif month == 6:
        if day < 21:
            sign = 'Gemini'
        else:
            sign = 'Cancer'

    elif month == 7:
        if day < 22:
            sign = 'Cancer'
        else:
            sign = 'Leo'

    elif month == 8:
        if day < 22:
            sign = 'Leo'
        else:
            sign = 'Virgo'

    elif month == 9:
        if day < 22:
            sign = 'Virgo'
        else:
            sign = 'Libra'

    elif month == 10:
        if day < 23:
            sign = 'Libra'
        else:
            sign = 'Scorpio'

    elif month == 11:
        if day < 22:
            sign = 'Scorpio'
        else:
            sign = 'Sagittarius'

    return sign



