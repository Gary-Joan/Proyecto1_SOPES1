#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <asm/uaccess.h>
#include <linux/sched/signal.h>
#include <linux/sched.h>
 

#define PROCFS_NAME "cpu_200915609"


struct task_struct *task;          
struct task_struct *task_child;    
struct list_head *list;  

static int cpu_show(struct seq_file *m, void *v){
    seq_printf(m, "Carne: 200915609 \n");
    seq_printf(m, "Nombre: Gary Joan Ortiz Lopez \n");
    int numeroProceso = 0;
    int total_time = 0;
    int seconds = 0; 
    int cpu_usage = 0;
    int cpu_total;
    for_each_process(task){
        total_time = task->utime + task->stime;
        
        seconds = task->utime - (task->start_time / hz);
        cpu_usage = 100 * ((total_time/ hz)/seconds);
        list_for_each(list, &task->children){                        
 
            task_child = list_entry( list, struct task_struct, sibling );    
     
            total_time = total_time + task_child->utime +task_child->stime;
        } 
        seq_printf(m, "------------%d----------\n", numeroProceso);
        seq_printf(m, "HZ : %d \n", hz);
        seq_printf(m, "total time : %d \n", total_time);
        seq_printf(m, "seconds : %d \n", seconds);
        seq_printf(m, "CPU TIME : %d \n", cpu_usage);
        seq_printf(m, "Nombre: %s \n", task->comm);
        seq_printf(m, "Estado: ");
        switch(task->state){
            case 0:
                seq_printf(m, "Ejecutando\n");
                break;
            case 1:
                seq_printf(m, "Listo\n");
                break;
            case 2:
                seq_printf(m, "Durmiendo\n");
                break;
            case 4:
                seq_printf(m, "Zombie\n");
                break;
            case 8:
                seq_printf(m, "Detenido\n");
                break;
            case 32:
                seq_printf(m, "En Espera\n");
                break;
        }
    }
    return 0;
}

static int cpu_open(struct inode *inode, struct file *file){
return single_open(file, cpu_show, NULL);
}

static const struct file_operations cpu_fops = {
    .owner = THIS_MODULE,
    .open = cpu_open,
    .read = seq_read,
    .llseek = seq_lseek,
    .release = single_release,
};

static int ver_cpu_init(void){
	printk(KERN_INFO "Cargando modulo cpu.\r\n");
	proc_create(PROCFS_NAME, 0, NULL, &cpu_fops);
	printk(KERN_INFO "Nombre : Gary Joan Ortiz Lopez \n Carnet : 200915609 \n Completado. Procceso: /proc/%s.\r\n", PROCFS_NAME);
	return 0;
}

static void ver_cpu_exit(void){
        
        printk(KERN_INFO "Modulo CPU Deshabilitado.\r\n");
        remove_proc_entry(PROCFS_NAME, NULL);		        
}

module_init(ver_cpu_init);
module_exit(ver_cpu_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("HB");
MODULE_DESCRIPTION("ejemplo de como menejar cpu");
