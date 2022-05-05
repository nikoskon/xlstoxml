from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
import pandas as pd
from lxml import etree as et

ws = Tk()
ws.title('xls2xml')
ws.geometry('800x400')


def xls2xml():
    raw_data = pd.read_excel(abs_path, sheet_name='XML_E7', converters={
                             'f_yphkoothta': str, 'f_afm': str, 'f_amka': str, 'f_afm_proswpoy': str})
    # root = et.Element("{http://www.yeka.gr/E7}AnaggeliesE7")
    xhtml_namespace = "http://www.yeka.gr/E7"
    xhtml = "{%s}" % xhtml_namespace
    nsmap = {'ns2': xhtml_namespace}
    root = et.Element(xhtml + "AnaggeliesE7", nsmap=nsmap)

    # ==> This is a loop that takes runs through each record and populates for each tag.
    for row in raw_data.iterrows():
        root_tags = et.SubElement(root, 'AnaggeliaE7')  # === > Root name
# These are the tag names for each row (SECTION 1)
        Column_heading_f_aa_pararthmatos = et.SubElement(
            root_tags, 'f_aa_pararthmatos')
        Column_heading_f_rel_protocol = et.SubElement(
            root_tags, 'f_rel_protocol')
        Column_heading_f_rel_date = et.SubElement(root_tags, 'f_rel_date')
        Column_heading_f_ypiresia_sepe = et.SubElement(
            root_tags, 'f_ypiresia_sepe')
        Column_heading_f_ypiresia_oaed = et.SubElement(
            root_tags, 'f_ypiresia_oaed')
        Column_heading_f_ergodotikh_organwsh = et.SubElement(
            root_tags, 'f_ergodotikh_organwsh')
        Column_heading_f_kad_kyria = et.SubElement(root_tags, 'f_kad_kyria')
        Column_heading_f_kad_deyt_1 = et.SubElement(root_tags, 'f_kad_deyt_1')
        Column_heading_f_kad_deyt_2 = et.SubElement(root_tags, 'f_kad_deyt_2')
        Column_heading_f_kad_deyt_3 = et.SubElement(root_tags, 'f_kad_deyt_3')
        Column_heading_f_kad_deyt_4 = et.SubElement(root_tags, 'f_kad_deyt_4')
        Column_heading_f_kad_pararthmatos = et.SubElement(
            root_tags, 'f_kad_pararthmatos')
        Column_heading_f_kallikratis_pararthmatos = et.SubElement(
            root_tags, 'f_kallikratis_pararthmatos')
        Column_heading_f_eponymo = et.SubElement(root_tags, 'f_eponymo')
        Column_heading_f_onoma = et.SubElement(root_tags, 'f_onoma')
        Column_heading_f_eponymo_patros = et.SubElement(
            root_tags, 'f_eponymo_patros')
        Column_heading_f_onoma_patros = et.SubElement(
            root_tags, 'f_onoma_patros')
        Column_heading_f_eponymo_mitros = et.SubElement(
            root_tags, 'f_eponymo_mitros')
        Column_heading_f_onoma_mitros = et.SubElement(
            root_tags, 'f_onoma_mitros')
        Column_heading_f_topos_gennhshs = et.SubElement(
            root_tags, 'f_topos_gennhshs')
        Column_heading_f_birthdate = et.SubElement(root_tags, 'f_birthdate')
        Column_heading_f_sex = et.SubElement(root_tags, 'f_sex')
        Column_heading_f_yphkoothta = et.SubElement(root_tags, 'f_yphkoothta')
        Column_heading_f_typos_taytothtas = et.SubElement(
            root_tags, 'f_typos_taytothtas')
        Column_heading_f_ar_taytothtas = et.SubElement(
            root_tags, 'f_ar_taytothtas')
        Column_heading_f_ekdousa_arxh = et.SubElement(
            root_tags, 'f_ekdousa_arxh')
        Column_heading_f_date_ekdosis = et.SubElement(
            root_tags, 'f_date_ekdosis')
        Column_heading_f_date_ekdosis_lixi = et.SubElement(
            root_tags, 'f_date_ekdosis_lixi')
        Column_heading_f_res_permit_inst = et.SubElement(
            root_tags, 'f_res_permit_inst')
        Column_heading_f_res_permit_inst_type = et.SubElement(
            root_tags, 'f_res_permit_inst_type')
        Column_heading_f_res_permit_inst_ar = et.SubElement(
            root_tags, 'f_res_permit_inst_ar')
        Column_heading_f_res_permit_inst_lixi = et.SubElement(
            root_tags, 'f_res_permit_inst_lixi')
        Column_heading_f_res_permit_ap = et.SubElement(
            root_tags, 'f_res_permit_ap')
        Column_heading_f_res_permit_ap_type = et.SubElement(
            root_tags, 'f_res_permit_ap_type')
        Column_heading_f_res_permit_ap_ar = et.SubElement(
            root_tags, 'f_res_permit_ap_ar')
        Column_heading_f_res_permit_ap_lixi = et.SubElement(
            root_tags, 'f_res_permit_ap_lixi')
        Column_heading_f_res_permit_visa = et.SubElement(
            root_tags, 'f_res_permit_visa')
        Column_heading_f_res_permit_visa_ar = et.SubElement(
            root_tags, 'f_res_permit_visa_ar')
        Column_heading_f_res_permit_visa_from = et.SubElement(
            root_tags, 'f_res_permit_visa_from')
        Column_heading_f_res_permit_visa_to = et.SubElement(
            root_tags, 'f_res_permit_visa_to')
        Column_heading_f_marital_status = et.SubElement(
            root_tags, 'f_marital_status')
        Column_heading_f_arithmos_teknon = et.SubElement(
            root_tags, 'f_arithmos_teknon')
        Column_heading_f_afm = et.SubElement(root_tags, 'f_afm')
        Column_heading_f_doy = et.SubElement(root_tags, 'f_doy')
        Column_heading_f_amika = et.SubElement(root_tags, 'f_amika')
        Column_heading_f_amka = et.SubElement(root_tags, 'f_amka')
        Column_heading_f_code_anergias = et.SubElement(
            root_tags, 'f_code_anergias')
        Column_heading_f_ar_vivliou_anilikou = et.SubElement(
            root_tags, 'f_ar_vivliou_anilikou')
        Column_heading_f_dieythinsi = et.SubElement(root_tags, 'f_dieythinsi')
        Column_heading_f_kallikratis = et.SubElement(
            root_tags, 'f_kallikratis')
        Column_heading_f_tk = et.SubElement(root_tags, 'f_tk')
        Column_heading_f_til = et.SubElement(root_tags, 'f_til')
        Column_heading_f_fax = et.SubElement(root_tags, 'f_fax')
        Column_heading_f_email = et.SubElement(root_tags, 'f_email')
        Column_heading_f_epipedo_morfosis = et.SubElement(
            root_tags, 'f_epipedo_morfosis')
        Column_heading_f_professional_education = et.SubElement(
            root_tags, 'f_professional_education')
        Column_heading_f_expertise_field = et.SubElement(
            root_tags, 'f_expertise_field')
        Column_heading_f_subject_area = et.SubElement(
            root_tags, 'f_subject_area')
        Column_heading_f_subject_group = et.SubElement(
            root_tags, 'f_subject_group')
        Column_heading_f_education_agency = et.SubElement(
            root_tags, 'f_education_agency')
        Column_heading_f_education_date_from = et.SubElement(
            root_tags, 'f_education_date_from')
        Column_heading_f_education_date_to = et.SubElement(
            root_tags, 'f_education_date_to')
        Column_heading_f_duration = et.SubElement(root_tags, 'f_duration')
        Column_heading_f_education_year = et.SubElement(
            root_tags, 'f_education_year')
        Column_heading_f_fl1 = et.SubElement(root_tags, 'f_fl1')
        Column_heading_f_fl2 = et.SubElement(root_tags, 'f_fl2')
        Column_heading_f_fl3 = et.SubElement(root_tags, 'f_fl3')
        Column_heading_f_fl4 = et.SubElement(root_tags, 'f_fl4')
        Column_heading_f_pc = et.SubElement(root_tags, 'f_pc')
        Column_heading_f_pc_other = et.SubElement(root_tags, 'f_pc_other')
        Column_heading_f_xaraktirismos = et.SubElement(
            root_tags, 'f_xaraktirismos')
        Column_heading_f_sxeshapasxolisis = et.SubElement(
            root_tags, 'f_sxeshapasxolisis')
        Column_heading_f_kathestosapasxolisis = et.SubElement(
            root_tags, 'f_kathestosapasxolisis')
        Column_heading_f_oros = et.SubElement(root_tags, 'f_oros')
        Column_heading_f_eidikothta = et.SubElement(root_tags, 'f_eidikothta')
        Column_heading_f_apodoxes = et.SubElement(root_tags, 'f_apodoxes')
        Column_heading_f_proslipsidate = et.SubElement(
            root_tags, 'f_proslipsidate')
        Column_heading_f_lixisymbashdate = et.SubElement(
            root_tags, 'f_lixisymbashdate')
        Column_heading_f_apolysisdate = et.SubElement(
            root_tags, 'f_apolysisdate')
        Column_heading_f_lastdaydate = et.SubElement(
            root_tags, 'f_lastdaydate')
        Column_heading_f_comments = et.SubElement(root_tags, 'f_comments')
        Column_heading_f_logosperatosis = et.SubElement(
            root_tags, 'f_logosperatosis')
        Column_heading_f_logosperatosiscomments = et.SubElement(
            root_tags, 'f_logosperatosiscomments')
        Column_heading_f_afm_proswpoy = et.SubElement(
            root_tags, 'f_afm_proswpoy')
        Column_heading_f_file = et.SubElement(root_tags, 'f_file')
        Column_heading_f_foreign_file = et.SubElement(
            root_tags, 'f_foreign_file')
        Column_heading_f_young_file = et.SubElement(root_tags, 'f_young_file')

        # These are the values that will be populated for each row above
# The values inside the [] are the raw file column headings.(SECTION 2)
        Column_heading_f_aa_pararthmatos.text = str(row[1]['f_aa_pararthmatos']) if str(
            row[1]['f_aa_pararthmatos']) != 'nan' else ""
        Column_heading_f_rel_protocol.text = str(row[1]['f_rel_protocol']) if str(
            row[1]['f_rel_protocol']) != 'nan' else ""
        Column_heading_f_rel_date.text = str(row[1]['f_rel_date']) if str(
            row[1]['f_rel_date']) != 'nan' else ""
        Column_heading_f_ypiresia_sepe.text = str(row[1]['f_ypiresia_sepe']) if str(
            row[1]['f_ypiresia_sepe']) != 'nan' else ""
        Column_heading_f_ypiresia_oaed.text = str(row[1]['f_ypiresia_oaed']) if str(
            row[1]['f_ypiresia_oaed']) != 'nan' else ""

        Column_heading_f_ergodotikh_organwsh.text = str(row[1]['f_ergodotikh_organwsh']) if str(
            row[1]['f_ergodotikh_organwsh']) != 'nan' else ""
        Column_heading_f_kad_kyria.text = str(row[1]['f_kad_kyria']) if str(
            row[1]['f_kad_kyria']) != 'nan' else ""
        Column_heading_f_kad_deyt_1.text = str(row[1]['f_kad_deyt_1']) if str(
            row[1]['f_kad_deyt_1']) != 'nan' else ""
        Column_heading_f_kad_deyt_2.text = str(row[1]['f_kad_deyt_2']) if str(
            row[1]['f_kad_deyt_2']) != 'nan' else ""
        Column_heading_f_kad_deyt_3.text = str(row[1]['f_kad_deyt_3']) if str(
            row[1]['f_kad_deyt_3']) != 'nan' else ""
        Column_heading_f_kad_deyt_4.text = str(row[1]['f_kad_deyt_4']) if str(
            row[1]['f_kad_deyt_4']) != 'nan' else ""
        Column_heading_f_kad_pararthmatos.text = str(row[1]['f_kad_pararthmatos']) if str(
            row[1]['f_kad_pararthmatos']) != 'nan' else ""
        Column_heading_f_kallikratis_pararthmatos.text = str(row[1]['f_kallikratis_pararthmatos']) if str(
            row[1]['f_kallikratis_pararthmatos']) != 'nan' else ""
        Column_heading_f_eponymo.text = str(row[1]['f_eponymo']) if str(
            row[1]['f_eponymo']) != 'nan' else ""
        Column_heading_f_onoma.text = str(row[1]['f_onoma']) if str(
            row[1]['f_onoma']) != 'nan' else ""
        Column_heading_f_eponymo_patros.text = str(row[1]['f_eponymo_patros']) if str(
            row[1]['f_eponymo_patros']) != 'nan' else ""
        Column_heading_f_onoma_patros.text = str(row[1]['f_onoma_patros']) if str(
            row[1]['f_onoma_patros']) != 'nan' else ""
        Column_heading_f_eponymo_mitros.text = str(row[1]['f_eponymo_mitros']) if str(
            row[1]['f_eponymo_mitros']) != 'nan' else ""
        Column_heading_f_onoma_mitros.text = str(row[1]['f_onoma_mitros']) if str(
            row[1]['f_onoma_mitros']) != 'nan' else ""
        Column_heading_f_topos_gennhshs.text = str(row[1]['f_topos_gennhshs']) if str(
            row[1]['f_topos_gennhshs']) != 'nan' else ""
        Column_heading_f_birthdate.text = str(row[1]['f_birthdate']) if str(
            row[1]['f_birthdate']) != 'nan' else ""
        Column_heading_f_sex.text = str(row[1]['f_sex']) if str(
            row[1]['f_sex']) != 'nan' else ""
        Column_heading_f_yphkoothta.text = str(row[1]['f_yphkoothta']) if str(
            row[1]['f_yphkoothta']) != 'nan' else ""
        Column_heading_f_typos_taytothtas.text = str(row[1]['f_typos_taytothtas']) if str(
            row[1]['f_typos_taytothtas']) != 'nan' else ""
        Column_heading_f_ar_taytothtas.text = str(row[1]['f_ar_taytothtas']) if str(
            row[1]['f_ar_taytothtas']) != 'nan' else ""
        Column_heading_f_ekdousa_arxh.text = str(row[1]['f_ekdousa_arxh']) if str(
            row[1]['f_ekdousa_arxh']) != 'nan' else ""
        Column_heading_f_date_ekdosis.text = str(row[1]['f_date_ekdosis']) if str(
            row[1]['f_date_ekdosis']) != 'nan' else ""
        Column_heading_f_date_ekdosis_lixi.text = str(row[1]['f_date_ekdosis_lixi']) if str(
            row[1]['f_date_ekdosis_lixi']) != 'nan' else ""
        Column_heading_f_res_permit_inst.text = str(row[1]['f_res_permit_inst']) if str(
            row[1]['f_res_permit_inst']) != 'nan' else ""
        Column_heading_f_res_permit_inst_type.text = str(row[1]['f_res_permit_inst_type']) if str(
            row[1]['f_res_permit_inst_type']) != 'nan' else ""
        Column_heading_f_res_permit_inst_ar.text = str(row[1]['f_res_permit_inst_ar']) if str(
            row[1]['f_res_permit_inst_ar']) != 'nan' else ""
        Column_heading_f_res_permit_inst_lixi.text = str(row[1]['f_res_permit_inst_lixi']) if str(
            row[1]['f_res_permit_inst_lixi']) != 'nan' else ""
        Column_heading_f_res_permit_ap.text = str(row[1]['f_res_permit_ap']) if str(
            row[1]['f_res_permit_ap']) != 'nan' else ""
        Column_heading_f_res_permit_ap_type.text = str(row[1]['f_res_permit_ap_type']) if str(
            row[1]['f_res_permit_ap_type']) != 'nan' else ""
        Column_heading_f_res_permit_ap_ar.text = str(row[1]['f_res_permit_ap_ar']) if str(
            row[1]['f_res_permit_ap_ar']) != 'nan' else ""
        Column_heading_f_res_permit_ap_lixi.text = str(row[1]['f_res_permit_ap_lixi']) if str(
            row[1]['f_res_permit_ap_lixi']) != 'nan' else ""
        Column_heading_f_res_permit_visa.text = str(row[1]['f_res_permit_visa']) if str(
            row[1]['f_res_permit_visa']) != 'nan' else ""
        Column_heading_f_res_permit_visa_ar.text = str(row[1]['f_res_permit_visa_ar']) if str(
            row[1]['f_res_permit_visa_ar']) != 'nan' else ""
        Column_heading_f_res_permit_visa_from.text = str(row[1]['f_res_permit_visa_from']) if str(
            row[1]['f_res_permit_visa_from']) != 'nan' else ""
        Column_heading_f_res_permit_visa_to.text = str(row[1]['f_res_permit_visa_to']) if str(
            row[1]['f_res_permit_visa_to']) != 'nan' else ""
        Column_heading_f_marital_status.text = str(row[1]['f_marital_status']) if str(
            row[1]['f_marital_status']) != 'nan' else ""
        Column_heading_f_arithmos_teknon.text = str(row[1]['f_arithmos_teknon']) if str(
            row[1]['f_arithmos_teknon']) != 'nan' else ""
        Column_heading_f_afm.text = str(row[1]['f_afm']) if str(
            row[1]['f_afm']) != 'nan' else ""
        Column_heading_f_doy.text = str(row[1]['f_doy']) if str(
            row[1]['f_doy']) != 'nan' else ""
        Column_heading_f_amika.text = str(row[1]['f_amika']) if str(
            row[1]['f_amika']) != 'nan' else ""
        Column_heading_f_amka.text = str(row[1]['f_amka']) if str(
            row[1]['f_amka']) != 'nan' else ""
        Column_heading_f_code_anergias.text = str(row[1]['f_code_anergias']) if str(
            row[1]['f_code_anergias']) != 'nan' else ""
        Column_heading_f_ar_vivliou_anilikou.text = str(row[1]['f_ar_vivliou_anilikou']) if str(
            row[1]['f_ar_vivliou_anilikou']) != 'nan' else ""
        Column_heading_f_dieythinsi.text = str(row[1]['f_dieythinsi']) if str(
            row[1]['f_dieythinsi']) != 'nan' else ""
        Column_heading_f_kallikratis.text = str(row[1]['f_kallikratis']) if str(
            row[1]['f_kallikratis']) != 'nan' else ""
        Column_heading_f_tk.text = str(row[1]['f_tk']) if str(
            row[1]['f_tk']) != 'nan' else ""
        Column_heading_f_til.text = str(row[1]['f_til']) if str(
            row[1]['f_til']) != 'nan' else ""
        Column_heading_f_fax.text = str(row[1]['f_fax']) if str(
            row[1]['f_fax']) != 'nan' else ""
        Column_heading_f_email.text = str(row[1]['f_email']) if str(
            row[1]['f_email']) != 'nan' else ""
        Column_heading_f_epipedo_morfosis.text = str(row[1]['f_epipedo_morfosis']) if str(
            row[1]['f_epipedo_morfosis']) != 'nan' else ""
        Column_heading_f_professional_education.text = str(row[1]['f_professional_education']) if str(
            row[1]['f_professional_education']) != 'nan' else ""
        Column_heading_f_expertise_field.text = str(row[1]['f_expertise_field']) if str(
            row[1]['f_expertise_field']) != 'nan' else ""
        Column_heading_f_subject_area.text = str(row[1]['f_subject_area']) if str(
            row[1]['f_subject_area']) != 'nan' else ""
        Column_heading_f_subject_group.text = str(row[1]['f_subject_group']) if str(
            row[1]['f_subject_group']) != 'nan' else ""
        Column_heading_f_education_agency.text = str(row[1]['f_education_agency']) if str(
            row[1]['f_education_agency']) != 'nan' else ""
        Column_heading_f_education_date_from.text = str(row[1]['f_education_date_from']) if str(
            row[1]['f_education_date_from']) != 'nan' else ""
        Column_heading_f_education_date_to.text = str(row[1]['f_education_date_to']) if str(
            row[1]['f_education_date_to']) != 'nan' else ""
        Column_heading_f_duration.text = str(row[1]['f_duration']) if str(
            row[1]['f_duration']) != 'nan' else ""
        Column_heading_f_education_year.text = str(row[1]['f_education_year']) if str(
            row[1]['f_education_year']) != 'nan' else ""
        Column_heading_f_fl1.text = str(row[1]['f_fl1']) if str(
            row[1]['f_fl1']) != 'nan' else ""
        Column_heading_f_fl2.text = str(row[1]['f_fl2']) if str(
            row[1]['f_fl2']) != 'nan' else ""
        Column_heading_f_fl3.text = str(row[1]['f_fl3']) if str(
            row[1]['f_fl3']) != 'nan' else ""
        Column_heading_f_fl4.text = str(row[1]['f_fl4']) if str(
            row[1]['f_fl4']) != 'nan' else ""
        Column_heading_f_pc.text = str(row[1]['f_pc']) if str(
            row[1]['f_pc']) != 'nan' else ""
        Column_heading_f_pc_other.text = str(row[1]['f_pc_other']) if str(
            row[1]['f_pc_other']) != 'nan' else ""
        Column_heading_f_xaraktirismos.text = str(row[1]['f_xaraktirismos']) if str(
            row[1]['f_xaraktirismos']) != 'nan' else ""
        Column_heading_f_sxeshapasxolisis.text = str(row[1]['f_sxeshapasxolisis']) if str(
            row[1]['f_sxeshapasxolisis']) != 'nan' else ""
        Column_heading_f_kathestosapasxolisis.text = str(row[1]['f_kathestosapasxolisis']) if str(
            row[1]['f_kathestosapasxolisis']) != 'nan' else ""
        Column_heading_f_oros.text = str(row[1]['f_oros']) if str(
            row[1]['f_oros']) != 'nan' else ""
        Column_heading_f_eidikothta.text = str(row[1]['f_eidikothta']) if str(
            row[1]['f_eidikothta']) != 'nan' else ""
        Column_heading_f_apodoxes.text = str(row[1]['f_apodoxes']) if str(
            row[1]['f_apodoxes']) != 'nan' else ""
        Column_heading_f_proslipsidate.text = str(row[1]['f_proslipsidate']) if str(
            row[1]['f_proslipsidate']) != 'nan' else ""
        Column_heading_f_lixisymbashdate.text = str(row[1]['f_lixisymbashdate']) if str(
            row[1]['f_lixisymbashdate']) != 'nan' else ""
        Column_heading_f_apolysisdate.text = str(row[1]['f_apolysisdate']) if str(
            row[1]['f_apolysisdate']) != 'nan' else ""
        Column_heading_f_lastdaydate.text = str(row[1]['f_lastdaydate']) if str(
            row[1]['f_lastdaydate']) != 'nan' else ""
        Column_heading_f_comments.text = str(row[1]['f_comments']) if str(
            row[1]['f_comments']) != 'nan' else ""
        Column_heading_f_logosperatosis.text = str(row[1]['f_logosperatosis']) if str(
            row[1]['f_logosperatosis']) != 'nan' else ""
        Column_heading_f_logosperatosiscomments.text = str(row[1]['f_logosperatosiscomments']) if str(
            row[1]['f_logosperatosiscomments']) != 'nan' else ""
        Column_heading_f_afm_proswpoy.text = str(row[1]['f_afm_proswpoy']) if str(
            row[1]['f_afm_proswpoy']) != 'nan' else ""
        Column_heading_f_file.text = str(row[1]['f_file']) if str(
            row[1]['f_file']) != 'nan' else ""
        Column_heading_f_foreign_file.text = str(row[1]['f_foreign_file']) if str(
            row[1]['f_foreign_file']) != 'nan' else ""
        Column_heading_f_young_file.text = str(row[1]['f_young_file']) if str(
            row[1]['f_young_file']) != 'nan' else ""
    # This Section outputs the data to an xml file
    # Unless you tell it otherwise it saves it to the same folder as the script.
    # ==> The variable tree is to hold all the values of "root"
    tree = et.ElementTree(root)
    # ===> This just formats in a way that the XML is readable
    et.indent(tree, space="\t", level=0)
    # ==> The data is saved to an XML file
    tree.write('output.xml', encoding="utf-8")


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Excel Files', '*xlsx')])
    if file_path is not None:
        global abs_path
        abs_path = file_path.name
        print("path=", file_path.name)


def uploadFiles():
    xls2xml()
    pb1 = Progressbar(
        ws,
        orient=HORIZONTAL,
        length=300,
        mode='determinate'
    )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text='XML File created Successfully!',
          foreground='green').grid(row=4, columnspan=3, pady=10)


adhar = Label(
    ws,
    text='Upload File only MS excel format '
)
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
    ws,
    text='Choose File',
    command=lambda: open_file()
)
adharbtn.grid(row=0, column=1)


upld = Button(
    ws,
    text='Create XML File',
    command=uploadFiles
)
upld.grid(row=3, columnspan=3, pady=10)


ws.mainloop()
