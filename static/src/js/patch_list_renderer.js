/** @odoo-module */
import {ListRenderer} from "@web/views/list/list_renderer"
import {patch} from "@web/core/utils/patch";

patch(ListRenderer.prototype, "benoit_recipe_widget", {
    /**
     * Patch the list to render multiple times the tables
     * @override
     */

    getCustomList(records, str_to_filter_by_filters){
        
        console.log(records);

        if (str_to_filter_by_filters){
            return records.filter((record) => (!record.data.name) || (record.data.name.includes(str_to_filter_by_filters)));
        }
        return records;
    }
});