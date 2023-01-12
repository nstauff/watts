
"""
This example demonstrates how to use WATTS to perform 
ACCERT simulations. The ACCERT model quotes the total cost 
and the cost of each account for a given set of parameters. 
Results from ACCERT are extracted and stored in params.
"""

import watts

# Set required parameters
params = watts.Parameters()
params['thermal_power'] = 3200
params['electric_power'] = 1300
params['cost_217'] = 29000000
input_name = "ACCERT_input.tmpl"


accert_plugin = watts.PluginACCERT(f'{input_name}')
accert_result = accert_plugin(params)

print(accert_result.inputs)
print(accert_result.outputs)
print("Total reactor cost [$]: ", accert_result.total_cost)

# ### uncomment below to see the ACCERT account table
print(accert_result.account_table.to_markdown())

params.show_summary(show_metadata=True, sort_by='key')

