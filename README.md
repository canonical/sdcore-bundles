# SD-Core bundles for K8s
[![CharmHub Badge](https://charmhub.io/sdcore-k8s/badge.svg)](https://charmhub.io/sdcore-k8s)
[![CharmHub Badge](https://charmhub.io/sdcore-control-plane-k8s/badge.svg)](https://charmhub.io/sdcore-control-plane-k8s)
[![CharmHub Badge](https://charmhub.io/sdcore-user-plane-k8s/badge.svg)](https://charmhub.io/sdcore-user-plane-k8s)

This project contains charm bundles for SD-Core. 

### Bundle generation

To render a bundle and output it in the bundle directory (e.g., `SDCORE_USER_PLANE`):

```bash
python3 -m venv env
source env/bin/activate
pip3 install -r render_bundle/requirements.txt
python3 render_bundle/render_bundle.py --bundle_variant SDCORE_USER_PLANE --output_file bundle/bundle.yaml
```
