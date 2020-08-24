import os
import modify_photo as modp
import manager_of_path


def manage_image(mp,classes_of_modified):
    total_classes = 500
    train_classes = 400  # 400
    validation_classes = 100
    i = 0
    j = 0
    if mp.setting_type_folder:
        indix_of_classes=slice(len(classes_of_modified))
    else:
        indix_of_classes=0
    vt=True
    while i < train_classes + validation_classes:
        if i ==train_classes:
            vt=False
            j=0
        name = str(i).zfill(4)
        path_image = mp.get_image_path(name)
        file = os.listdir(path_image)
        list = modp.open_cv2(path_image, file)
        j=modify_photo(classes_of_modified[indix_of_classes],mp,list,j,vt)
        print(path_image)
        print(file)
        i = i + 1
        if not mp.setting_type_folder:
            indix_of_classes=(indix_of_classes+1)%len(classes_of_modified)


def modify_photo(classes,mp,list,j,tv):
    #tv:
    # -true=train
    # -false=validation
    if tv:
        string_tv="train"
    else:
        string_tv="validation"
    tv_modified=string_tv+"_modified"
    tv_original=string_tv+"_original"
    j_modified_tot=j
   #if not mp.setting_type_folder:
    #    j_modified_tot=j*len(classes)-1

    if "50_death_pixels" in classes:
            j_modified_tot = modp.dead_pixel_50(list, j_modified_tot, mp.get_path_classes("50_death_pixels")[tv_modified])
            j_original = modp.not_modified(list, j, mp.get_path_classes("50_death_pixels")[tv_original])
            if mp.setting_type_folder:
                j_modified_tot=j
    if "200_death_pixels" in classes:
        j_modified_tot = modp.dead_pixel_200(list, j_modified_tot, mp.get_path_classes("200_death_pixels")[tv_modified])
        j_original = modp.not_modified(list, j, mp.get_path_classes("200_death_pixels")[tv_original])
        if mp.setting_type_folder:
            j_modified_tot = j
    if "blur" in classes:
            j_modified_tot = modp.blur(list, j_modified_tot, mp.get_path_classes("blur")[tv_modified])
            j_original = modp.not_modified(list, j, mp.get_path_classes("blur")[tv_original])
            if mp.setting_type_folder:
                j_modified_tot = j

    if "black" in classes:
            j_modified_tot = modp.black(list, j_modified_tot, mp.get_path_classes("black")[tv_modified])
            j_original = modp.not_modified(list, j, mp.get_path_classes("black")[tv_original])
            if mp.setting_type_folder:
                j_modified_tot=j

    if "brightness" in classes:
            j_modified_tot = modp.brightness(list, j_modified_tot, mp.get_path_classes("brightness")[tv_modified])
            j_original = modp.not_modified(list, j, mp.get_path_classes("brightness")[tv_original])
            if mp.setting_type_folder:
                j_modified_tot=j
    return j_original
<<<<<<< HEAD
path = "/media/pietro/Volume/Ubuntu/home/pietro/Documenti/Unifi/tirocinio/img/" #"/home/bernabei/carla0.8.4/PythonClient/_out/"
classes_of_modified=["blur","black","brightness","50_death_pixels","200_death_pixels"]
mp = manager_of_path.ManagerOfPath(path,classes_of_modified,True)
manage_image(mp,classes_of_modified[4])
=======
path =  "/home/bernabei/carla0.8.4/PythonClient/_out/" #"/media/pietro/Volume/Ubuntu/home/pietro/Documenti/Unifi/tirocinio/img/"
classes_of_modified=["blur","black","brightness","50_death_pixels"]
mp = manager_of_path.ManagerOfPath(path,classes_of_modified,False)
manage_image(mp,classes_of_modified)
>>>>>>> a785dbd735bcb11b6aeabe1ea3a19153b1641ad3
