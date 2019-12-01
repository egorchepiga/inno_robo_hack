def watch_on_zero(fedor):
    try:
        fedor.rotate_head(0, 0, 0, absolute=True)
    except BrokenPipeError:
        print('broken pipe')
        fedor.start_socket_shit()
        watch_on_zero(fedor)

def watch_on_target(fedor):
    try:
        fedor.rotate_head(30, 20, 0, absolute=True)
    except BrokenPipeError:
        print('broken pipe')
        fedor.start_socket_shit()
        watch_on_target(fedor)

def watch_on_box(fedor):
    try:
        fedor.rotate_head(-10, 15, 0, absolute=True)
    except BrokenPipeError:
        print('broken pipe')
        fedor.start_socket_shit()
        watch_on_box(fedor)

