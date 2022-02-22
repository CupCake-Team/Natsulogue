label natsuki_room:
    if renpy.windows or renpy.linux:
        show mask_2
        show mask_3
        show room_mask
        show room_mask2
        show monika_bg zorder 1
    else:
        show space1 as rw1:
            size(270, 180)
            pos(50, 200)

        show space2 as rw2:
            size(270, 180)
            pos(925, 200)
        show monika_bg zorder 1
    pass
