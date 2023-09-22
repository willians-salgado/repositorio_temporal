from odoo import fields, models

class MyRecipe(models.Model):
    _name = "my.recipe"
    _description = "my.recipe"

    recipe_name = fields.Char(tracking=True)
    serve_ids = fields.Many2many(
        "product.attribute.value",
    )

    active = fields.Boolean(default=True, tracking=True)

    ingredient_ids = fields.One2many(
        comodel_name="my.recipe.line", inverse_name="recipe_id"
    )
