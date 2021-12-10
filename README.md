# MacSmbMount

Plugin for [fman.io](https://fman.io) that enables you mount and unmount SMB file shares directly from [fman.io](https://fman.io).

You can install this plugin by pressing `<shift+cmd+p>` to open the command pallet. Then type `install plugin`. Look for the `MacSmbMount` plugin and select it.

## Mount a SMB share

The functions are available via the Command Pallete. Just press `<shift+cmd+p>` and search for `Mount smb volume`. A dialogue will pop up where you can enter the server address of your share.

If you did not store your credentials in the keychain, a finder window will appear asking you for your credentials.

If you entered the full address of the shared volume e.g. `local.share/MyVolume` `MyVolume` will be mounted.

If you just entered a server address e.g. `local.share` a finder pop up will appear giving you the option to choose the volume you would like to mount. By selecting a Volume the volume will be mounted.

## Unmount a shared volume

To unmount a volume, enter the Command Pallete by pressing `<shift+cmd+p>` and searching for `Unmount volume`. A dialogue will appear that lists all your currently mounted Volumes. Select the one you would like to eject and it will be ejected.
