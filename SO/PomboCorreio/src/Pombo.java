import java.util.Scanner;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class Pombo extends Thread{

    private int n;      //tamanhoMochila;
    private int tc;     //tempoColeta;
    private int tv;     //tempoVoo;
    private int td;     //tempoDescarga;


    public Pombo(int tamanhoMochila, int tempoColeta, int tempoVoo, int tempoDescarga) {
        this.n = tamanhoMochila;
        this.tc = tempoColeta;
        this.tv = tempoVoo;
        this.td = tempoDescarga;
    }

    public Pombo criarPombo(){

        int tamanhoMochila;
        int tempoColeta;
        int tempoVoo;
        int tempoDescarga;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Tamanho da mochila: ");
        tamanhoMochila = scanner.nextInt();
        System.out.print("\n");

        System.out.print("Tempo para coletar as mensagens: ");
        tempoColeta = scanner.nextInt();
        System.out.print("\n");

        System.out.print("Tempo para descarregar as máquinas: ");
        tempoDescarga = scanner.nextInt();
        System.out.print("\n");

        System.out.print("Tempo de voo: ");
        tempoVoo = scanner.nextInt();
        System.out.print("\n");

        Pombo pombo = new Pombo(tamanhoMochila, tempoColeta, tempoVoo, tempoDescarga);

        return pombo;
    }

/*
    public Pombo eliminarPombo(){

    }
*/
    @Override
    public void run() {

        while(true){

            System.out.println("Dormindo...zzZ");
            System.out.println("Coletando cartas...");
            System.out.println("Voando de A para B...");
            System.out.println("Descarregando cartas...");
            System.out.println("Voando de B para A...");
        }
    }

}
