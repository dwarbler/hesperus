### About
The RaspberryPi-based server code for hesperus, receiving, decoding and normalizing ADS-B data with an RTL-SDR.

### Dependencies
This project requires a local installation of `librtlsdr` to allow for data reading. It can be installed on Mac with homebrew
```
>> brew install librtlsdr
```

The required Python dependencies can be found in the project [pyproject.toml](pyproject.toml) and can be installed with pip as follows
```
>> pip install .
```

The project uses the Pyright LSP and the Ruff linter. These can be altered/configured in the [pyproject.toml](pyproject.toml) file.
