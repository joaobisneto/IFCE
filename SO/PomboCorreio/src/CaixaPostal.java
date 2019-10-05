import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class CaixaPostal extends Thread{

    private int m;
    private int mensagem;
    private boolean disponivel;
    private BlockingQueue<Integer> caixaPostal = new ArrayBlockingQueue<>(m);

    public CaixaPostal(int tamanhoCaixaPostal){
        this.m = tamanhoCaixaPostal;
    }

    public synchronized void postarCartas(int idUsuario) throws InterruptedException{

        Random random = new Random(100);

        while(disponivel == true){
            System.out.println("O Usuário #" + idUsuario + " esperando...");
            wait();
        }
        if(caixaPostal.size() < m){
            mensagem = random.nextInt(100);
            caixaPostal.put(mensagem);
        }
        System.out.println("O Usuário #" + idUsuario + " postou uma mensagem.");
        disponivel = true;
        notifyAll();
    }

    public synchronized void coletarCartas() throws InterruptedException{

        Random random = new Random();

        while(disponivel == false){
            System.out.println("O pombo está coletando as mensagens...");
            wait();
        }
        if(random.nextInt(m) == 0){
            mensagem = caixaPostal.take();
        }
        System.out.println("O pombo coletou todas as mensagens.");
        disponivel = false;
        notifyAll();
    }

    public synchronized void esvaziarCaixaPostal(int tamanhoCaixaPostal){
        for(int i=0; i<caixaPostal.size(); i++){
            caixaPostal.remove(i);
        }
    }


    public void eliminarUsuario(int identificacao){
        for(int i=0; i<usuarios.size(); i++){
            if((usuarios.get(i)).id == identificacao) {
                usuarios.remove(i);
            }
        }
        System.out.println("Usuário #" + identificacao + "foi eliminado.");
    }
}
