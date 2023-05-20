# sdcore-bundles

This project contains charm bundles for the SD-CORE.

### Usage

Render the bundle:

```bash
export PYTHONPATH=$(pwd)
pip install -r requirements.txt
python3 src/render_bundle.py --bundle_variant SDCORE_UP
```

By default, the bundle will be generated in the project root directory under `bundle.yaml`.
