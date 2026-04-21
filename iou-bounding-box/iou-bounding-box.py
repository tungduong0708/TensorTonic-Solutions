def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    area_A = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_B = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    x_1 = max(box_a[0], box_b[0])
    y_1 = max(box_a[1], box_b[1])
    x_2 = min(box_a[2], box_b[2])
    y_2 = min(box_a[3], box_b[3])

    # print(x_1, y_1, x_2, y_2)
    if x_2 > x_1 and y_2 > y_1:
        area_I = (x_2 - x_1) * (y_2 - y_1)
    else:
        area_I = 0
    print(area_I)
    area_U = area_A + area_B - area_I

    return area_I/area_U