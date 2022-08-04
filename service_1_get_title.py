def title_from_path(output_file_name):
    title =  output_file_name.split("/", 2)[2].split(".")[0]
    return title
