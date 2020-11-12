import os
import modify_photo as modp
import manager_of_path


def manage_image(mp, classes_of_modified):
    total_classes = 24#500
    train_classes = 24 # 400
    validation_classes =0 #100
    i = 0
    j = 0
    if mp.setting_type_folder:
        indix_of_classes = slice(len(classes_of_modified))
    else:
        indix_of_classes = 0
    vt = True
    while i < train_classes + validation_classes:
        if i == train_classes:
            vt = False
            j = 0
        name = str(i).zfill(4)
        path_image = mp.get_image_path(name)
        file = os.listdir(path_image)
        list = modp.open_cv2(path_image, file)
        j = modify_photo(classes_of_modified[indix_of_classes], mp, list, j, vt)
        print(path_image)
        print(file)
        i = i + 1
        if not mp.setting_type_folder:
            indix_of_classes = (indix_of_classes + 1) % len(classes_of_modified)


def modify_photo(classes, mp, list_original, j, tv):
    # tv:
    # -true=train
    # -false=validation

    if tv:
        string_tv = "train"
    else:
        string_tv = "validation"
    tv_modified = string_tv + "_modified"
    tv_original = string_tv + "_original"
    j_modified_tot = j
    # if not mp.setting_type_folder:
    #    j_modified_tot=j*len(classes)-1

    overlap_broken=["broken1.png","broken7.png","broken8.jpg"]

    overlap_ice=["ice.jpg","ice3.png"]

    overlap_banding=["banding1.jpg"]
    list=list_original[:]
    tv=[]
    for i in range(len(classes)):
        tv.append(tv_original)
    for cl in classes:
        tv[classes.index(cl)]=tv_modified


        j_original = modp.not_modified(list_original, j, mp.get_path_classes(cl)[tv_original])
        j_modified_tot = modp.dead_pixel_50(list, j_modified_tot, mp.get_path_classes(cl)[tv[0]])
        j_modified_tot = modp.dead_pixel_200(list, j_modified_tot, mp.get_path_classes(cl)[tv[1]])
        j_modified_tot = modp.blur(list, j_modified_tot, mp.get_path_classes(cl)[tv[2]])
        j_modified_tot = modp.black(list, j_modified_tot, mp.get_path_classes(cl)[tv[3]])
        j_modified_tot = modp.brightness(list, j_modified_tot, mp.get_path_classes(cl)[tv[4]])
        j_modified_tot = modp.greyscale(list, j_modified_tot, mp.get_path_classes(cl)[tv[5]])
        j_modified_tot = modp.nodemos(list, j_modified_tot, mp.get_path_classes(cl)[tv[6]])
        j_modified_tot = modp.noise(list, j_modified_tot, mp.get_path_classes(cl)[tv[7]])
        j_modified_tot = modp.sharpness(list, j_modified_tot, mp.get_path_classes(cl)[tv[8]])
        j_modified_tot = modp.overlap(list, j_modified_tot, mp.get_path_classes(cl)[tv[9]],mp.path_of_classes+overlap_broken[0],0.35)
        j_modified_tot = modp.overlap(list, j_modified_tot, mp.get_path_classes(cl)[tv[10]],mp.path_of_classes+overlap_ice[0],0.2)
        j_modified_tot = modp.banding(list, j_modified_tot, mp.get_path_classes(cl)[tv[11]])
        j_modified_tot = modp.condensation(list, j_modified_tot, mp.get_path_classes(cl)[tv[12]])
        j_modified_tot = modp.dirty_lens(list, j_modified_tot, mp.get_path_classes(cl)[tv[13]])
        j_modified_tot = modp.chromaticaberration(list, j_modified_tot, mp.get_path_classes(cl)[tv[14]])
        j_modified_tot = modp.rain(list, j_modified_tot, mp.get_path_classes(cl)[tv[15]])

        return j_original



path = "/home/pietro/Documenti/Unifi/tirocinio/img"#"/home/bernabei/carla0.8.4/PythonClient/_out/" #"/home/bernabei/carla0.8.4/PythonClient/_out_prima_run/" #"/media/pietro/Volume/Ubuntu/home/pietro/Documenti/Unifi/tirocinio/img/"
classes_of_modified = ["blur", "black", "brightness",  "200_death_pixels","nodemos","noise","sharpness","brokenlens","icelens","banding","50_death_pixels","greyscale","condensation","dirty_lens","chromaticaberration","rain"]
mp = manager_of_path.ManagerOfPath(path, classes_of_modified, True)
manage_image(mp, classes_of_modified)




