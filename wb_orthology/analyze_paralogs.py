# A [hopefully] simple script for comparing orthologs from WormBase to those at the Alliance.

import pprint

filename = 'paralogs_only.ace'
with open(filename, "r") as f:
    orthologs = {}
    for line in f:
        if line.startswith('Gene :'):
            # Extract string between first pair of quotes.
            extracted_name = line.split('"')[1]
            orthologs[extracted_name] = {}
            continue
        if line.startswith('Gene_info'):
            matching_gene = line.split('"')[5]
            # Check if dictionary already exists.
            if not matching_gene in orthologs[extracted_name].keys():
                orthologs[extracted_name][matching_gene] = []
            try:
                species = line.split('"')[9]
            except:
                print(line)

            try:
                algorithm = line.split('"')[15]
            except:
                print(line)

            try:
                date = line.split('"')[17]
            except:
                print(line)  

            orthologs[extracted_name][matching_gene].append((species, algorithm, date))

species_set = set()
algorithm_set = set()
total_set = set()
algorithm_count = 0

for item in orthologs.keys():
    for sub_item in orthologs[item].keys():
        printed_item_already = False
        for item_from_list in orthologs[item][sub_item]:
            # if item_from_list[0] == 'Saccharomyces cerevisiae':
            #     if printed_item_already is False:
            #         print(item)
            #         printed_item_already = True
            #     print(sub_item)
            #     print(item_from_list)
            total_set.add(item_from_list)
            species_set.add(item_from_list[0])
            algorithm_set.add(item_from_list[1])
            if item_from_list[1] == 'modENCODE_Pseudogenes':
                algorithm_count+=1

# Pretty print algorithm set.
print('Algorithms:')
pprint.pprint(algorithm_set)

# Pretty print species set.
print('Species:')
pprint.pprint(species_set)

# for item in total_set:
#     if item[0] == 'Homo sapiens':
#         

print(algorithm_count)