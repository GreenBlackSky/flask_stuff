from flask_assets import Bundle


def compile_assets(assets):
    js_bundle = Bundle('src/js/script.js', filters='jsmin', output='dst/js/script.min.js')
    assets.register('scripts_assets', js_bundle)
    js_bundle.build()
