def bouncingBall(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        view = 1
        while h * bounce > window:
            h = h * bounce
            view += 2
        return view

    else:
        return - 1


bouncingBall(3, 0.66, 1.5)
