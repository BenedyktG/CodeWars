class Rectangle:

    @staticmethod
    def rect_into_rects(lng, wdth):
        result = []
        if lng == wdth or lng == 0 or wdth == 0:
            return None
        while (lng * wdth) > 0:
            if lng < wdth:
                result.append(lng)
                wdth -= lng
            else:
                result.append(wdth)
                lng -= wdth
        print(result)


def test(a, b):
    Rectangle.rect_into_rects(a, b)


test(22, 6)
test(13, 4)
