import aspectlib


@aspectlib.Aspect(bind=True)
def resource_logging_aspect(cutpoint, *args):
    print("Resource Logging: Start resource logging")
    print(f"Resource Logging: running: {cutpoint.__name__}")
    print(f"Resource Logging: Current resources status: {args[0].resources}")

    yield

    print(f"Resource Logging: Final resources status: {args[0].resources}")


@aspectlib.Aspect(bind=True)
def transaction_aspect(cutpoint, *args):
    print("Transaction: Starting transaction...")
    print(f"Transaction: Running method: {cutpoint.__name__}")
    print(f"Transaction: Current money: {args[0].money}")

    yield

    print(f"Transaction: Final money: {args[0].money}")
