def example():
    from my_structlog import my_structlog

    log = my_structlog.get_logger("some_logger")
    log.debug("debugging is hard", a_list=[1, 2, 3])
    log.info("informative!", some_key="some_value")
    log.warning("uh-uh!")
    log.info("informative!")
    log.error("omg", a_dict={"a": 42, "b": "foo"})
    log.critical("wtf", what="Restart")

    log2 = my_structlog.get_logger("another_logger")
    try:
        log.debug("Exception example")
        d = {"x": 42}
        print(d["y"], "foo")
    except KeyError:
        log2.exception("poor me", stack_info=True)
    log.info("all better now!")


if __name__ == '__main__':
    example()
