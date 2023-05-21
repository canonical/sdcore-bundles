# sdcore-bundles

This project contains charm bundles for the SD-CORE.

### Bundle generation

To render the `SDCORE_UP` bundle and output it in the `bundle` directory:

```bash
pip3 install -r render_bundle/requirements.txt
python3 render_bundle/render_bundle.py --bundle_variant SDCORE_UP --output_file bundle/bundle.yaml
```
