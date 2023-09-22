from odoo import fields, models

class RecipeLines(models.Model):
    _name = "my.recipe.line"
    _description = "my.recipe.line"

    product_tmpl_id = fields.Many2one(
        "product.template"
    )
    apply_on_variants_ids = fields.Many2many("product.attribute.value")
    # serve = fields.Many2one("product.attribute.value",
    #                         domain=[("attribute_id.name","=","Serve")])
    recipe_id = fields.Many2one(comodel_name="my.recipe")
