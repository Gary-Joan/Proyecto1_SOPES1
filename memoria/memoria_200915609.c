#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <asm/uaccess.h>
/* to get works meminfo */
#include <linux/hugetlb.h>
#include <linux/mm.h>
#include <linux/mman.h>
#include <linux/mmzone.h>
#include <linux/quicklist.h>
#include <linux/swap.h>
#include <linux/vmstat.h>
#include <linux/atomic.h>
#include <asm/page.h>
#include <asm/pgtable.h>

#define PROCFS_NAME "memoria_200915609"

struct sysinfo i;
unsigned long committed;
unsigned long allowed;
//struct vmalloc_info vmi;
long cached;
unsigned long pages[NR_LRU_LISTS];
int lru;

static int memori_show(struct seq_file *m, void *v){

int porcentaje = 0;
seq_printf(m,"{");
seq_printf(m,"\"Nombre\": \"Gary Joan Ortiz Lopez\",\n");
seq_printf(m,"\"Carnet\": 200915609 ,\n");
#define K(x) ((x) << (PAGE_SHIFT - 10))
si_meminfo(&i); 

porcentaje = (i.freeram*100)/i.totalram;
seq_printf(m,"\"MemTotal\": %8lu ,\n",K(i.totalram));
seq_printf(m,"\"MemFree\": %8lu ,\n",K(i.freeram));
seq_printf(m,"\"Buffers\": %8lu ,\n",K(i.bufferram));
seq_printf(m, "\"Porcentaje Libre\": %8u\n",porcentaje);

#ifdef CONFIG_HIGHMEM
seq_printf(m,"\"HighTotal\": %8lu ,\n",K(i.totalhigh));
seq_printf(m,"\"HighFree\": %8lu ,\n",K(i.freehigh));
seq_printf(m,"\"LowTotal\": %8lu ,\n",K(i.totalram-i.totalhigh));
seq_printf(m,"\"LowFree\": %8lu \n",K(i.freeram-i.freehigh));
#endif
seq_printf(m,"}\n");

#undef K
return 0;
}

static int memori_open(struct inode *inode, struct file *file){
return single_open(file, memori_show, NULL);
}

static const struct file_operations memori_fops = {
.owner = THIS_MODULE,
.open = memori_open,
.read = seq_read,
.llseek = seq_lseek,
.release = single_release,
};

static int __init memori_init(void){
printk(KERN_INFO "Cargando modulo memoria_200915609.\r\n");
proc_create(PROCFS_NAME, 0, NULL, &memori_fops);
printk(KERN_INFO "Nombre : Gary Joan Ortiz Lopez \n Carnet : 200915609 \n Completado. Procceso: /proc/%s.\r\n", PROCFS_NAME);
return 0;
}

static void __exit memori_exit(void){

printk(KERN_INFO "Modulo memoria Deshabilitado.\r\n");
remove_proc_entry(PROCFS_NAME, NULL);
}

module_init(memori_init);
module_exit(memori_exit);

MODULE_LICENSE("GPL");
