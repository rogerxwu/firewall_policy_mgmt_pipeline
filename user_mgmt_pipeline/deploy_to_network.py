# use naplam to deploy the change to the device


import napalm
import sys
import os
import argparse


def main(config_file):
    # parse
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('-username')
    parser.add_argument('-password')
    args = parser.parse_args()

    """Load a config for the device."""

    """ if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        msg = "Missing or invalid config file {0}".format(config_file)
        raise ValueError(msg) """

    print("Loading config file {0}.".format(config_file))

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver("junos")

    # Connect:
    device = driver(
        hostname="192.168.223.2",
        username=args.username,
        password=args.password,
    )

    print("Opening ...")
    device.open()

    # replace
    #print("Loading replacement candidate ...")
    #device.load_replace_candidate(filename=config_file)
    # merge
    print("Loading merge candidate ...")
    device.load_merge_candidate(filename=config_file)

    # Note that the changes have not been applied yet. Before applying
    # the configuration you can check the changes:
    print("\nDiff:")
    print(device.compare_config())

    # You can commit or discard the candidate changes.
    try:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    except NameError:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == "y":
        print("Committing ...")
        device.commit_config()
    else:
        print("Discarding ...")
        device.discard_config()

    """ print("Committing ...")
    device.commit_config() """
    # close the session with the device.
    device.close()
    print("Done.")


if __name__ == "__main__":
    #if len(sys.argv) < 2:
    #   print('Please supply the full path to "new_good.conf"')
    #    sys.exit(1)
    #config_file = sys.argv[1]
    config_file = './user.cfg'
    main(config_file)