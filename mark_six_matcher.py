import re
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def get_mark_six():
    # Redirect Chrome log to a file
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration to prevent some issues
    chrome_options.add_argument('--log-level=3')  # Set log level to SEVERE

    url = "https://bet.hkjc.com/marksix/Results.aspx?lang=ch"

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Wait for the resultMainTable element to be present
    try:
        result_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultMainTable"))
        )

        html_source = driver.page_source

        soup = BeautifulSoup(html_source, 'html.parser')

        # Find the div with id 'resultMainTable'
        result_table = soup.find('div', {'id': 'resultMainTable'})

        # Check if the result_table is found
        if result_table:
            # Find the first div with class 'resultMainRow'
            row = result_table.find('div', {'class': 'resultMainRow'})

            if row:
                result_number = row.find('div', {'class': 'resultMainCell1'}).text.strip()

                # Extracting the numbers from the image titles or alt text using regex
                images = row.find_all('img')

                # Check if images is not None
                if images:
                    image_numbers = [
                        re.search(r'no_(\d+)_s', img['src']).group(1) if re.search(r'no_(\d+)_s', img['src']) else '' for img in images]

                    # Filter out blank elements
                    image_numbers = list(filter(None, image_numbers))
                    
                    return str(result_number), image_numbers
                else:
                    print(f"No image found for result number: {result_number}")
        else:
            print("Unable to find 'resultMainTable' on the webpage.")
    except Exception:
        print(f"exception occurred : Timeout")
        
    finally:
        # Close the browser
        driver.quit()
        
def my_num_match(mark_six):
    # my_mark_six = [['03', '09', '30', '33', '34', '43'],
    #                ['09', '13', '24', '38', '39', '44'],
    #                ['06', '07', '19', '26', '40', '49'],
    #                ['03', '08', '23', '35', '37', '47'],
    #                ['04', '06', '16', '24', '27', '44','48']]
    my_mark_six = [['01','07','13','27','39','41'],
                   ['03','08','09','35','36','44'],
                   ['11','15','23','28','30','37'],
                   ['04','12','26','34','48','49'],
                   ['05','10','17','18','33','42'],
                   ['06','16','24','32','40','47'],
                   ['14','21','25','31','38','43'],
                   ['02','19','20','22','29','45'],
                   ['46','01','07','08','13','27'],
                   ['02','03','05','15','28','37'],
                   ['04','17','33','36','40','42'],
                   ['09','11','16','23','32','43'],
                   ['10','14','24','38','41','48'],
                   ['12','20','25','26','34','44'],
                   ['06','18','19','21','35','47'],
                   ['22','29','30','31','39','46'],
                   ['01','07','13','27','45','49']]
    
    for my_list in my_mark_six:
        count = 0
        for my_num in my_list:
            if my_num in mark_six[1]:
                if my_num in mark_six[1][6]:
                    count += 0.5
                else:
                    count += 1
        print(f'list {my_list}, matched = {count}')
        
def custom_list_entry():   
    custom_list_input :list[str] = input("enter your list (format: 1 2 3 47 48 49) Enter 0 to Exit: ").split(" ")
    for index, num in enumerate(custom_list_input):
        if 1 <= int(num) <= 9: 
            custom_list_input[index] = '0' + num
    wrapped_list = [custom_list_input]
    # for multi list entry only
    if custom_list_input == ['0']:
        return 0 
    return wrapped_list

def custom_entry_multi_list():  
    multi_list = []
    while (True):
        custom_list = custom_list_entry()
        if (custom_list == 0):
            break
        else:
            multi_list += custom_list
    return multi_list
                
def custom_match(custom_list, mark_six_result):
    for mark_six_list in custom_list:
        count = 0
        for num in mark_six_list:
            if num in mark_six_result[1]:
                if num in mark_six_result[1][6]:
                    count += 0.5
                else:
                    count += 1
        print(f'list: {mark_six_list}, matched = {count}')

def mark_six_output():
        mark_six = get_mark_six()
        if not mark_six:
            exit()
        print(f"期數: {mark_six[0]}\n 號碼: {mark_six[1]}")
        return mark_six

def main():
    choice = 0
    choice : str = input('1:my number\n2:custom list (single)\n3:custom list (multi)\ninput: ')
    
    if choice == '1':
        mark_six = mark_six_output()
        my_num_match(mark_six)
        
    elif choice == '2':
        custom_list = custom_list_entry()
        mark_six = mark_six_output()
        custom_match(custom_list, mark_six)
        
    elif choice == '3':
        custom_list = custom_entry_multi_list()
        mark_six = mark_six_output()
        custom_match(custom_list, mark_six) 
           
if __name__ == "__main__":     
    main()
