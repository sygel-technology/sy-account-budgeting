import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-account-budgeting",
    description="Meta package for sygel-technology-sy-account-budgeting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_budget_propagate_date>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
