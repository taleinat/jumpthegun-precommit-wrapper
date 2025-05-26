from functools import wraps


def main():
    import pre_commit.languages.python

    # Install hook wrapper.
    orig_run_hook = pre_commit.languages.python.run_hook
    @wraps(orig_run_hook)
    def wrapped_run_hook(prefix, entry, args, file_args, **kwargs):
        entry = "jumpthegun run " + entry
        print(f"{entry = }")
        return orig_run_hook(prefix, entry, args, file_args, **kwargs)
    pre_commit.languages.python.run_hook = wrapped_run_hook

    # Run pre-commit.
    import pre_commit.main
    raise SystemExit(pre_commit.main.main())


if __name__ == "__main__":
    main()
