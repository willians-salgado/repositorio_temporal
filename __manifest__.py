{
    "name": "Benoit Recipe Widget",
    "summary": """
    Benoit Recipe Widget
    """,
    "author": "Willians Salgado",
    "depends": ["base", "web", "account", "sale", "sale_management", "stock", "sale_stock"],
    "license": "AGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "views/my_recipe_views.xml",
        "views/my_recipe_line_views.xml",
        "views/my_recipe_menu_views.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "benoit_recipe_widget/static/src/js/**/*",
            "benoit_recipe_widget/static/src/xml/**/*"
        ]
    },
    "application": False
}